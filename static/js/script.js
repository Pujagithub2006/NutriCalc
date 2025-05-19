document.addEventListener('DOMContentLoaded', () => {
    let foodData = [];


    // searchInput.disabled = true;

    fetch('/food')
        .then(response => response.json())
        .then(data => {
            console.log('Loaded data:', data);  // Check in browser console
            foodData = data;
        });

    const searchInput = document.getElementById('searchInput');
    const suggestions = document.getElementById('suggestions');
    const foodDetails = document.getElementById('foodDetails');

    // searchInput.disabled = true; // disable initially

    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase();
        suggestions.innerHTML = '';

        const filtered = foodData.filter(item =>
            item['Food Items'] && item['Food Items'].toLowerCase().includes(query)
        );

        filtered.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item['Food Items'];
            li.addEventListener('click', () => showDetails(item));
            suggestions.appendChild(li);
        });
    });

    function showDetails(item) {
        foodDetails.innerHTML = `
            <h2>${item['Food Items']}</h2>
            <p>Energy: ${item['Energy kcal']} kcal</p>
            <p>Carbs: ${item['Carbs']} g</p>
            <p>Protein: ${item['Protein(g)']} g</p>
            <p>Fat: ${item['Fat(g)']} g</p>
            <p>Free Sugar: ${item['Freesugar(g)']} g</p>
            <p>Fibre: ${item['Fibre(g)']} g</p>
            <p>Cholesterol: ${item['Cholestrol(mg)']} mg</p>
            <p>Calcium: ${item['Calcium(mg)']} mg</p>
        `;

    }

    // 📷 Image upload logic and model prediction
    const imageUpload = document.getElementById('imageUpload');

    imageUpload.addEventListener('change', async function () {
        const file = this.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('image', file);

        try {
            const res = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                body: formData
            });
            const data = await res.json();
            if (data.prediction) {
                searchInput.value = data.prediction;
                searchInput.dispatchEvent(new Event('input'));
            } else {
                alert('Prediction failed');
            }
        } catch (err) {
            console.error('Prediction error:', err);
        }
    });

  // your current JS code here
});
