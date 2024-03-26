$.ajax({
    url: '/api/data',
    type: 'GET',
    success: function(data) {
        // Process data and update visualizations
    },
    error: function(xhr, status, error) {
        console.error(error);
    }
});
