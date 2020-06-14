const BtnDelete = document.querySelectorAll(".btn-delete")

if (BtnDelete){
	const BtnArray = Array.from(BtnDelete);
	BtnArray.forEach((btn) => {
		btn.addEventListener("click", (e) => {
			if (!confirm("¿Estas Seguro Que Deseas Eliminar?")) {
				e.preventDefault();
			}
		});
	});
}