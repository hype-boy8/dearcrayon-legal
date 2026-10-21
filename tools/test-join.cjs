// Run with node tools/test-join.cjs after generating join/index.html.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, '../join/index.html'), 'utf8');
const code = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1];
const token = '1.ABCDEFGHIJKLMNOP.abcdefghijklmnopqrstuvwxyz012345';
function setup({hash='#'+token, lang='ko', ua='Desktop', platform='', touches=0, clipboard=true, released=false}={}) {
  const elements = new Map();
  function element(id) {
    if (!elements.has(id)) elements.set(id, {id, hidden:false, textContent:'', value:'', attributes:{}, children:[], handlers:{},
      setAttribute(k,v){this.attributes[k]=v;}, removeAttribute(k){delete this.attributes[k]; if(k==='href') delete this.href;},
      replaceChildren(){this.children=[];}, appendChild(child){this.children.push(child);},
      addEventListener(k,f){this.handlers[k]=f;}, focus(){this.focused=true;}, select(){this.selected=true;},
      querySelectorAll(){return links;}, closest(){return this;}});
    return elements.get(id);
  }
  const links = ['ko','en','de','fr','es','ja'].map(l=>Object.assign(element(l), {hreflang:l}));
  const location = new URL('https://example.test/join/?lang='+lang+hash);
  const document = {documentElement:{},getElementById:element,createElement:()=>({textContent:'',children:[],appendChild(c){this.children.push(c);}})};
  const window = {handlers:{}, addEventListener(k,f){this.handlers[k]=f;}};
  let copied;
  const navigator = {languages:['ko'],userAgent:ua,platform,maxTouchPoints:touches};
  if (clipboard) navigator.clipboard={writeText:async x=>{copied=x;}};
  const history={replaceState(_a,_b,url){location.href=url.href;}};
  vm.runInNewContext(released?code.replace('var AVAILABLE = false;', 'var AVAILABLE = true;'):code, {document,window,navigator,location,history,URL,URLSearchParams});
  return {element,links,location,document,window,copied:()=>copied};
}
(async function(){
  for(const hash of ['', '#broken', '#'+token+'x', '#1.ABCDEFGHIJKLMNOP.<script>']) {
    const p=setup({hash}); assert.equal(p.element('open').hidden,true); assert.equal(p.element('open').href,undefined); assert.equal(p.element('guide-wrap').hidden,true); assert.equal(p.element('bad').hidden,false);
  }
  const p=setup();
  assert.equal(p.element('open').href,'dearcrayon://join/'+token);
  assert.equal(p.element('open').hidden,false);
  assert.equal(p.element('get').href,'../');
  assert.equal(p.element('join-footer').hidden,true);
  for(const link of p.links) {
    let prevented=false;
    p.element('languages').handlers.click({target:link,preventDefault(){prevented=true;}});
    assert.equal(prevented,true); assert.equal(p.location.hash,'#'+token);
    assert.equal(p.location.search,'?lang='+link.hreflang);
    assert.equal(p.document.documentElement.lang,link.hreflang);
    assert.equal(p.element('open').href,'dearcrayon://join/'+token);
  }
  p.element('copy').handlers.click(); await Promise.resolve();
  assert.equal(new URL(p.copied()).hash,'#'+token);
  assert.equal(p.element('copy').textContent,'コピーしました');
  p.location.hash='#bad'; p.window.handlers.hashchange();
  assert.equal(p.element('open').hidden,true); assert.equal(p.element('guide-wrap').hidden,true);
  const fallback=setup({clipboard:false}); fallback.element('copy').handlers.click();
  assert.equal(fallback.element('manual-copy').hidden,false);
  assert.equal(new URL(fallback.element('manual-link').value).hash,'#'+token);
  assert.equal(fallback.element('manual-link').selected,true);
  for (const opts of [{ua:'iPhone'},{platform:'MacIntel',touches:5}]) {
    const i=setup(opts); assert.equal(i.element('ios').hidden,false); assert.equal(i.element('open').hidden,true);
  }
  const android=setup({ua:'Android'}).element('open').href;
  assert.ok(android.startsWith('intent://join/'+token+'#Intent;scheme=dearcrayon;package=com.dearcrayon.app;'));
  assert.ok(android.includes('S.browser_fallback_url=https%3A%2F%2Fexample.test%2F;end'));
  const launched=setup({ua:'Android',released:true});
  assert.ok(launched.element('get').href.startsWith('https://play.google.com/'));
  assert.equal(launched.element('join-footer').hidden,false);
  assert.ok(launched.element('open').href.includes('S.browser_fallback_url=https%3A%2F%2Fplay.google.com'));
  assert.equal(setup({lang:'unsupported'}).document.documentElement.lang,'ko');
  assert.equal(setup({lang:'constructor'}).document.documentElement.lang,'ko');
  assert.ok(html.includes('content="no-referrer"'));
  assert.ok(!/\b(?:fetch|localStorage|sessionStorage)\b/.test(code));
  console.log('PASS: valid/invalid links, six languages, fragment preservation, clipboard/fallback, iPhone/iPad, Android intent, pre/post launch');
})();
