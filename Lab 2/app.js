const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// static files 
app.use(express.static(path.join(__dirname)));

// Root route main page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Query String Parameter
app.get('/greet', (req, res) => {
  const name = req.query.name || 'Guest';
  res.send(`Hello, ${name}! Welcome to Blankhouse Collective.`);
});

// Path Parameter
app.get('/event/:eventName', (req, res) => {
  const event = req.params.eventName;
  res.send(`Details for event: ${event}`);
});

// Static Route
app.get('/community', (req, res) => {
  res.sendFile(path.join(__dirname, 'community.html'));
});

// Static Route
app.get('/society', (req, res) => {
  res.sendFile(path.join(__dirname, 'society.html'));
});

// Static Route
app.get('/wellness', (req, res) => {
  res.sendFile(path.join(__dirname, 'wellness.html'));
});

// Studios Page
app.get('/studios', (req, res) => {
  res.sendFile(path.join(__dirname, 'studios.html'));
});

app.listen(port, () => {
  console.log(`Blankhouse server running at http://localhost:${port}`);
});
