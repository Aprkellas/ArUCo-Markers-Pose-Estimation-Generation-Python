function selectImage() {
  // Trigger the file input element when the button is clicked
  document.getElementById("imageInput").click();

  // Listen for changes in the file input
  document.getElementById("imageInput").addEventListener("change", function () {
    // Get the selected file
    const selectedFile = this.files[0];

    if (selectedFile) {
      // You can now handle the selected file as needed
      console.log("Selected image file:", selectedFile);

      fetch();
    }
  });
}
