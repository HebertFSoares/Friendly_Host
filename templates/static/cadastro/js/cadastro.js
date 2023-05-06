document.getElementById("user-type").addEventListener("change", function() {
    var userType = this.value;
    
    var estudanteFields = document.querySelector(".estudante-fields");
    var anfitriaoFields = document.querySelector(".anfitriao-fields");
    
    if (userType === "estudante") {
      estudanteFields.style.display = "block";
      anfitriaoFields.style.display = "none";
    } else if (userType === "anfitriao") {
      estudanteFields.style.display = "none";
      anfitriaoFields.style.display = "block";
    } else {
      estudanteFields.style.display = "none";
      anfitriaoFields.style.display = "none";
    }
  });
  