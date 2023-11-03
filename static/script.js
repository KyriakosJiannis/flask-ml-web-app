function validateForm() {
    // Sepal Length validation
    var sepalLengthInput = document.getElementsByName("sepal_length")[0];
    var sepalLengthError = document.getElementById("sepal_length_error");
    var sepalLengthValue = parseFloat(sepalLengthInput.value);

    if (isNaN(sepalLengthValue) || sepalLengthValue < 4 || sepalLengthValue > 8.5) {
        sepalLengthError.innerHTML = "Value should be a number between 4 and 8.5";
        return false;
    } else {
        sepalLengthError.innerHTML = "";
    }

    // Sepal Width validation
    var sepalWidthInput = document.getElementsByName("sepal_width")[0];
    var sepalWidthError = document.getElementById("sepal_width_error");
    var sepalWidthValue = parseFloat(sepalWidthInput.value);

    if (isNaN(sepalWidthValue) || sepalWidthValue < 2 || sepalWidthValue > 5) {
        sepalWidthError.innerHTML = "Value should be a number between 2 and 5";
        return false;
    } else {
        sepalWidthError.innerHTML = "";
    }

    // Petal Length validation
    var petalLengthInput = document.getElementsByName("petal_length")[0];
    var petalLengthError = document.getElementById("petal_length_error");
    var petalLengthValue = parseFloat(petalLengthInput.value);

    if (isNaN(petalLengthValue) || petalLengthValue < 1 || petalLengthValue > 7) {
        petalLengthError.innerHTML = "Value should be a number between 1 and 7";
        return false;
    } else {
        petalLengthError.innerHTML = "";
    }

    // Petal Width validation
    var petalWidthInput = document.getElementsByName("petal_width")[0];
    var petalWidthError = document.getElementById("petal_width_error");
    var petalWidthValue = parseFloat(petalWidthInput.value);

    if (isNaN(petalWidthValue) || petalWidthValue < 0.05 || petalWidthValue > 3) {
        petalWidthError.innerHTML = "Value should be a number between 0.05 and 3";
        return false;
    } else {
        petalWidthError.innerHTML = "";
    }

    return true;
}
