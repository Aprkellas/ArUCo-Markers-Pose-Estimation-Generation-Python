async function selectImage() {
  try {
    // Trigger the file input element when the button is clicked
    document.getElementById("imageInput").click();

    // Listen for changes in the file input
    document
      .getElementById("imageInput")
      .addEventListener("change", async function () {
        // Get the selected file
        const selectedFile = this.files[0];

        if (selectedFile) {
          // You can now handle the selected file as needed
          console.log("Selected image file:", selectedFile);

          // Display a loading message or spinner while processing
          // For example: document.getElementById("loadingMessage").style.display = "block";

          // Create a FormData object to send the selected file
          const formData = new FormData();
          formData.append("image", selectedFile);

          // Send a POST request to the /detect endpoint and await the response
          const response = await fetch("/detect", {
            method: "POST",
            body: formData,
          });

          if (response.ok) {
            // If the response is successful, process it
            const blob = await response.blob();

            // Create an object URL from the response blob
            const imageUrl = URL.createObjectURL(blob);

            // Display the detected image in an <img> element
            const imgElement = document.getElementById("detectedImage");
            imgElement.src = imageUrl;
            imgElement.style = "display:flex";

            // Update the display with the detected results

            // Hide the loading message or spinner
            // For example: document.getElementById("loadingMessage").style.display = "none";
          } else {
            console.error("Failed to process image. Server returned an error.");
          }
        }
      });
  } catch (error) {
    console.error("An error occurred:", error);
  }
}
