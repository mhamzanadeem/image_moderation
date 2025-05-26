document.getElementById("moderate-form").addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission
    const token = document.getElementById("token").value;
    const file = document.getElementById("image").files[0];
    const formData = new FormData();
    formData.append("file", file); // Match backend's expected field name

    try {
        const response = await fetch("/moderate", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`
            },
            body: formData
        });
        const result = await response.json();
        document.getElementById("result").innerText = JSON.stringify(result, null, 2);
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error: " + error.message;
    }
});