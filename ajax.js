document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search').addEventListener('click', function() {
        const hyphen = /\-/g
        const sdate = document.getElementById('search_date').value.replace(hyphen, "");
        const formationNumber = document.getElementById('search_formation_number').value;
        const trainNumber = document.getElementById('search_train_number').value;
        const queryObject = {
            tnum: trainNumber,
            fnum: formationNumber,
        };

        const queryString = new URLSearchParams(queryObject);
        const url = "result.cgi/" + sdate + "?" + queryString;

        fetch(url, {
            method: "GET",
        })
        .then(function(response) {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(function(bodytext) {
            const resultBox = document.getElementById('resultbox');
            resultBox.textContent = bodytext;
        });

    }, false);
}, false);
