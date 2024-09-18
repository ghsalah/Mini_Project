
// Set active class on the current page
function setActiveNavItem() {
    const currentPage = window.location.pathname;
    const navItems = document.querySelectorAll('.sidebar-item');

    navItems.forEach(item => {
        if (item.getAttribute('href') === currentPage) {
            item.classList.add('main-active');
        } else {
            item.classList.remove('main-active');
        }
    });
}

// Initialize sidebar on page load
document.addEventListener('DOMContentLoaded', function() {
    setActiveNavItem(); // Set the active class on page load
});
