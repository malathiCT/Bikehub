document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.bike-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 120}ms`;
        card.classList.add('animate__animated', 'animate__fadeInUp');
    });

    const apiGrid = document.getElementById('api-bike-grid');
    if (apiGrid) {
        fetch('/api/bikes/?page=1&page_size=2')
            .then((response) => response.json())
            .then((data) => {
                if (!data.results || data.results.length === 0) {
                    apiGrid.innerHTML = '<div class="col-12 text-center text-white-50">No bikes available from the API yet.</div>';
                    return;
                }

                apiGrid.innerHTML = data.results.map((bike) => `
                    <div class="col-lg-6 col-md-12">
                        <div class="card bike-card h-100 overflow-hidden rounded-4">
                            <img src="${bike.display_image_url || bike.image_url || 'https://images.unsplash.com/photo-1511994298241-608e28f14fde?auto=format&fit=crop&w=900&q=80'}" class="card-img-top" alt="${bike.brand} ${bike.model}">
                            <div class="card-body">
                                <div class="d-flex justify-content-between align-items-start">
                                    <div>
                                        <span class="badge badge-accent mb-2">${bike.brand}</span>
                                        <h5 class="card-title fw-bold">${bike.model}</h5>
                                    </div>
                                    <span class="fw-bold text-danger">₹${bike.price}</span>
                                </div>
                                <p class="card-text text-white-50">${bike.description}</p>
                            </div>
                        </div>
                    </div>
                `).join('');
            })
            .catch(() => {
                apiGrid.innerHTML = '<div class="col-12 text-center text-white-50">Unable to load API bikes right now.</div>';
            });
    }
});
