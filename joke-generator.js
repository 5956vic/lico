#!/usr/bin/env node

const https = require('https');

/**
 * Fetch a random joke from JokeAPI
 * @param {string} category - Joke category (General, Programming, Knock-Knock, etc.)
 * @returns {Promise<Object>} Joke object
 */
function getJoke(category = 'Any') {
  return new Promise((resolve, reject) => {
    const url = `https://v2.jokeapi.dev/joke/${category}`;
    
    https.get(url, (res) => {
      let data = '';
      
      res.on('data', (chunk) => {
        data += chunk;
      });
      
      res.on('end', () => {
        try {
          const joke = JSON.parse(data);
          if (joke.error) {
            reject(new Error(`API Error: ${joke.message}`));
          } else {
            resolve(joke);
          }
        } catch (e) {
          reject(new Error('Failed to parse JSON response'));
        }
      });
    }).on('error', reject);
  });
}

/**
 * Format and display a joke
 * @param {Object} joke - Joke object from API
 */
function displayJoke(joke) {
  console.log('\n' + '='.repeat(50));
  if (joke.type === 'single') {
    console.log(joke.joke);
  } else {
    console.log('Setup: ' + joke.setup);
    console.log('\nPunchline: ' + joke.delivery);
  }
  console.log('='.repeat(50) + '\n');
}

/**
 * Main function
 */
async function main() {
  const categories = ['Any', 'General', 'Programming', 'Knock-Knock', 'Dark', 'Spooky'];
  
  try {
    console.log('🎭 Random Joke Generator\n');
    console.log('Fetching a random joke...');
    
    const randomCategory = categories[Math.floor(Math.random() * categories.length)];
    const joke = await getJoke(randomCategory);
    
    displayJoke(joke);
    console.log(`Category: ${randomCategory}`);
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { getJoke, displayJoke };