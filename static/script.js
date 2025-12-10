document.addEventListener('DOMContentLoaded', () => {
    const xmlInput = document.getElementById('xml-input');
    const jsonOutput = document.getElementById('json-output');
    const xmlToJsonBtn = document.getElementById('xml-to-json-btn');
    const copyJsonBtn = document.getElementById('copy-json-btn');

    const jsonInput = document.getElementById('json-input');
    const xmlOutput = document.getElementById('xml-output');
    const jsonToXmlBtn = document.getElementById('json-to-xml-btn');
    const copyXmlBtn = document.getElementById('copy-xml-btn');

    const dataTypeSelect = document.getElementById('dataType');

    const toggleSpinner = (btn, show) => {
        const spinner = btn.querySelector('.spinner-border');
        if (show) {
            spinner.classList.remove('d-none');
            btn.disabled = true;
        } else {
            spinner.classList.add('d-none');
            btn.disabled = false;
        }
    };

    xmlToJsonBtn.addEventListener('click', () => {
        const xmlData = xmlInput.value;
        if (xmlData) {
            const dataType = dataTypeSelect.value;
            toggleSpinner(xmlToJsonBtn, true);
            fetch(`/${dataType}/xml-to-json`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/xml'
                },
                body: xmlData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error('Error:', data.error);
                    jsonOutput.value = `Error: ${data.error}`;
                } else {
                    jsonOutput.value = JSON.stringify(data, null, 2);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                jsonOutput.value = 'Error converting XML to JSON.';
            })
            .finally(() => {
                toggleSpinner(xmlToJsonBtn, false);
            });
        }
    });

    jsonToXmlBtn.addEventListener('click', () => {
        const jsonData = jsonInput.value;
        if (jsonData) {
            const dataType = dataTypeSelect.value;
            toggleSpinner(jsonToXmlBtn, true);
            fetch(`/${dataType}/json-to-xml`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonData
            })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => { throw new Error(err.error) });
                }
                return response.text();
            })
            .then(data => {
                xmlOutput.value = data;
            })
            .catch(error => {
                console.error('Error:', error);
                xmlOutput.value = `Error: ${error.message}`;
            })
            .finally(() => {
                toggleSpinner(jsonToXmlBtn, false);
            });
        }
    });

    copyJsonBtn.addEventListener('click', () => {
        jsonOutput.select();
        document.execCommand('copy');
    });

    copyXmlBtn.addEventListener('click', () => {
        xmlOutput.select();
        document.execCommand('copy');
    });
});
