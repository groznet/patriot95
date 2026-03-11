// We don't load header.html, sidebar.html footer.html using JS anymore on Hugo

// Initialize sidebar functionality on mobile
document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay');
    const openBtn = document.getElementById('sidebar-open');
    const closeBtn = document.getElementById('sidebar-close');

    function toggleSidebar() {
        // Check if it's currently closed by looking for the translate class
        const isClosed = sidebar.classList.contains('translate-x-full');

        if (isClosed) {
            // OPENING
            sidebar.classList.remove('translate-x-full');
            overlay.classList.remove('hidden');
            // Small delay to allow the 'hidden' removal to register before fading in
            setTimeout(() => overlay.classList.add('opacity-100'), 10);
            document.body.classList.add('overflow-hidden');
        } else {
            // CLOSING
            sidebar.classList.add('translate-x-full');
            overlay.classList.remove('opacity-100');
            // Wait for transition (300ms) before hiding overlay entirely
            setTimeout(() => overlay.classList.add('hidden'), 300);
            document.body.classList.remove('overflow-hidden');
        }
    }

    // Now the main button toggles both ways
    openBtn.addEventListener('click', toggleSidebar);
    
    // These still explicitly close for a better user experience
    closeBtn.addEventListener('click', toggleSidebar);
    overlay.addEventListener('click', toggleSidebar);

    // ESC key support
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !sidebar.classList.contains('translate-x-full')) {
            toggleSidebar();
        }
    });
});