const express = require('express');
const fs = require('fs');
const path = require('path');
const axios = require('axios');

const app = express();
const port = 3000;
const orgName = 'NuePkgs';
const apiUrl = `https://api.github.com/orgs/${orgName}/members`;
const jsonFilePath = path.join(__dirname, 'gh-org-users.json');

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Endpoint to fetch members
app.get('/members', async (req, res) => {
  try {
    const response = await axios.get(apiUrl);
    const data = response.data;
    // Save data to JSON file
    fs.writeFileSync(jsonFilePath, JSON.stringify(data, null, 2));
    res.json(data);
  } catch (error) {
    console.error('Error fetching from API:', error);
    // Load data from file if API fails
    if (fs.existsSync(jsonFilePath)) {
      const data = JSON.parse(fs.readFileSync(jsonFilePath));
      res.json(data);
    } else {
      res.status(500).send('Unable to retrieve data.');
    }
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
