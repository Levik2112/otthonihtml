
function jelenlegiMenuPont(){
    const opciok = document.querySelectorAll('.opciok');
    console.log(opciok)
    const jelenURL = window.location.href;
    console.log(jelenURL)
  
    opciok.forEach(function(opcio) {       
        if (jelenURL.includes(opcio.href)) {
            opcio.classList.add('aktualis');
        }
    });
}
