// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    var yearFilter = document.getElementById('filter-year');
    var monthFilter = document.getElementById('filter-month');
    var tagsFilter = document.getElementById('filter-tags');
    var postList = document.getElementById('post-list');
    var posts = postList.getElementsByTagName('li');

    var years = new Set();
    var months = new Set();
    var tags = new Set();

    // Populate year, month, and tag filters
    for (var i = 0; i < posts.length; i++) {
        var post = posts[i];
        var year = post.getAttribute('data-year');
        var month = post.getAttribute('data-month');
        var postTags = post.getAttribute('data-tags').split(', ');

        years.add(year);
        months.add(month);
        postTags.forEach(tag => {
            if (tag) tags.add(tag);
        });
    }

    // Add unique years to the year filter
    years.forEach(year => {
        var option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        yearFilter.appendChild(option);
    });

    // Add unique months to the month filter
    months.forEach(month => {
        var option = document.createElement('option');
        option.value = month;
        option.textContent = month;
        monthFilter.appendChild(option);
    });

    // Add unique tags to the tags filter
    tags.forEach(tag => {
        var option = document.createElement('option');
        option.value = tag;
        option.textContent = tag;
        tagsFilter.appendChild(option);
    });

    // Function to filter posts based on selected filters
    function filterPosts() {
        var selectedYear = yearFilter.value;
        var selectedMonth = monthFilter.value;
        var selectedTag = tagsFilter.value.toLowerCase();

        for (var i = 0; i < posts.length; i++) {
            var post = posts[i];
            var postYear = post.getAttribute('data-year');
            var postMonth = post.getAttribute('data-month');
            var postTags = post.getAttribute('data-tags').toLowerCase();

            var yearMatch = selectedYear === '' || postYear === selectedYear;
            var monthMatch = selectedMonth === '' || postMonth === selectedMonth;
            var tagMatch = selectedTag === '' || postTags.includes(selectedTag);

            if (yearMatch && monthMatch && tagMatch) {
                post.style.display = '';
            } else {
                post.style.display = 'none';
            }
        }
    }

    // Event listeners for filter changes
    yearFilter.addEventListener('change', filterPosts);
    monthFilter.addEventListener('change', filterPosts);
    tagsFilter.addEventListener('change', filterPosts);
});
