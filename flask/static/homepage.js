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

      // Display the selected image
      const selectedImageUrl = URL.createObjectURL(selectedFile);
      const selectedImageElement = document.getElementById("selectedImage");
      selectedImageElement.src = selectedImageUrl;

      // Create a FormData object to send the selected file
      const formData = new FormData();
      formData.append("image", selectedFile);

      // Send a POST request to the /detect endpoint
      fetch("/detect", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.blob())
        .then((blob) => {
          // Create an object URL from the response blob
          const detectedImageUrl = URL.createObjectURL(blob);

          // Display the detected image
          const detectedImageElement = document.getElementById("detectedImage");
          detectedImageElement.src = detectedImageUrl;
        });
    }
  });
}
