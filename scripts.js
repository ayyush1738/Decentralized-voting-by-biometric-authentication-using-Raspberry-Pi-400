document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("Aadhar ID:", document.querySelector("#aadhar-id").value);
    console.log(
      "Aadhar Hash:",
      document.querySelector("#aadhar-hash").value
    );
  });

  document.addEventListener("DOMContentLoaded", function () {
    // Read the values from the file and update the input fields
    // Submit form to log details in console
    const form = document.querySelector("form");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      console.log("Aadhar ID:", document.querySelector("#aadhar-id").value);
      console.log(
        "Aadhar Hash:",
        document.querySelector("#aadhar-hash").value
      );
    });

    // Update input fields from file
    const updateInputFields = () => {
      const request = new XMLHttpRequest();
      request.onreadystatechange = () => {
        if (request.readyState === XMLHttpRequest.DONE) {
          if (request.status === 200) {
            const lines = request.responseText.split("\n");
            document.querySelector("#aadhar-id").value = lines[0];
            document.querySelector("#aadhar-hash").value = lines[1];
          } else {
            console.log("Error retrieving file:", request.status);
          }
        }
      };
      request.open("GET", "details.txt", true);
      request.send();
    };

    // Update input fields every 5 seconds
    setInterval(updateInputFields, 3000);
  });

  // function to display the "vote cast" animation
  function showVoteCast() {
    // hide the vote options
    document.querySelectorAll('.vote-option').forEach(function(element) {
        element.style.display = 'none';
    });
    
    // display the "vote cast" animation
    document.getElementById('vote-cast').style.display = 'block';
}

// add event listeners to the vote options
document.getElementById('party1').addEventListener('click', function() {
    showVoteCast();
});
document.getElementById('party2').addEventListener('click', function() {
    showVoteCast();
});
document.getElementById('party3').addEventListener('click', function() {
    showVoteCast();
});