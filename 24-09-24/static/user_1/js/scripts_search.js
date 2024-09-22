document.addEventListener("DOMContentLoaded", function() {
    // Handle Search Tabs
    window.openTab = function(evt, tabName) {
        var tablinks = document.getElementsByClassName("tab-btn");

        // Remove active3 from all tabs
        for (let i = 0; i < tablinks.length; i++) {
            tablinks[i].classList.remove("active3");
        }

        // Add active3 to the clicked tab
        evt.currentTarget.classList.add("active3");
    };

    // Handle Suggestions in Private Search Bar
    window.showSuggestions = function() {
        let input = document.getElementById("searchInput").value;
        let suggestions = document.getElementById("suggestions");

        if (input.length > 0) {
            suggestions.innerHTML = `
                <div class="search-item"><i class="fa fa-search"></i><p>${input} dev</p></div>
                <div class="search-item"><i class="fa fa-search"></i><p>${input}script</p></div>
                <div class="search-item"><i class="fa fa-search"></i><p>${input} and node</p></div>
                <div class="see-more"><a href="#">See More...</a></div>
            `;
        } else {
            suggestions.innerHTML = "";
        }
    };

    // Handle Modal Display for Results
    window.openModal = function() {
        document.getElementById("searchModal").style.display = "block";
    };

    window.closeModal = function() {
        document.getElementById("searchModal").style.display = "none";
    };

    window.clearSearch = function() {
        document.getElementById("searchInput").value = "";
        document.getElementById("suggestions").innerHTML = "";
    };
});
