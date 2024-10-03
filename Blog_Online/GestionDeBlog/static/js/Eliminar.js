(function (){
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn => {
        btn.addEventListener('click', e => {
            const confirmacion = confirm('¿Seguro de eliminar el registro seleccionado?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();