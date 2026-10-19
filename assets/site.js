document.querySelectorAll('.language').forEach(menu => {
 const trigger = menu.querySelector('summary');
 document.addEventListener('click', event => { if (!menu.contains(event.target)) menu.open = false; });
 menu.addEventListener('keydown', event => { if (event.key === 'Escape') { menu.open = false; trigger.focus(); } });
});
document.querySelectorAll('a[href="#receive"]').forEach(link => link.addEventListener('click', () => {
 const panel = document.getElementById('receive'); panel.open = true; panel.querySelector('summary').focus({preventScroll:true});
}));
