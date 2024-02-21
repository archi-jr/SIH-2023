const express = require('express');
const session = require('express-session');
const base64url = require('base64url');
const crypto = require('crypto');
const app = express();
const port = 3000;

app.use(express.json());
app.use(session({ secret: 'your-secret-key', resave: false, saveUninitialized: true }));

const users = {}; // Store users' data in memory (for demonstration purposes)

function generateChallenge() {
  return base64url.encode(crypto.randomBytes(32));
}

app.get('/register', (req, res) => {
  const challenge = generateChallenge();
  req.session.challenge = challenge;

  res.json({ challenge });
});

app.post('/register', (req, res) => {
  const { challenge, attestationObject, clientDataJSON } = req.body;
  // Validate and store the credential, associating it with the user (in-memory storage in this example)
  const userId = base64url.encode(crypto.randomBytes(16));
  users[userId] = { attestationObject, clientDataJSON };

  res.json({ success: true });
});

app.get('/login', (req, res) => {
  const challenge = generateChallenge();
  req.session.challenge = challenge;

  res.json({ challenge });
});

app.post('/login', (req, res) => {
  const { challenge, assertion, userId } = req.body;
  // Validate the assertion and authenticate the user (in-memory authentication in this example)
  const storedData = users[userId];
  if (!storedData) {
    res.json({ success: false, message: 'User not found' });
    return;
  }

  res.json({ success: true });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

