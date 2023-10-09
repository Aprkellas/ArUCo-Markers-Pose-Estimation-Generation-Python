async function selectImage() {
  try {
    document.getElementById("imageInput").click();

    document
      .getElementById("imageInput")
      .addEventListener("change", async function () {
        const selectedFile = this.files[0];

        if (selectedFile) {
          console.log("Selected image file:", selectedFile);

          const formData = new FormData();
          formData.append("image", selectedFile);

          const response = await fetch("/detect", {
            method: "POST",
            body: formData,
          });

          if (response.ok) {
            const blob = await response.blob();

            const imageUrl = URL.createObjectURL(blob);

            const imgElement = document.getElementById("detectedImage");
            imgElement.src = imageUrl;
            imgElement.style = "display:flex";

          } else {
            console.error("Failed to process image. Server returned an error.");
          }
        }
      });
  } catch (error) {
    console.error("An error occurred:", error);
  }
}
