/* eslint-disable */

// Add ES6 support
/* eslint-env es6 */

// Require Mongoose module
const mongoose = require('mongoose');

// Define Schema
const Schema = mongoose.Schema;

// Create reviews schema
const reviews = new Schema({
  id: {
    type: Number,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  dealership: {
    type: Number,
    required: true,
  },
  review: {
    type: String,
    required: true,
  },
  purchase: {
    type: Boolean,
    required: true,
  },
  purchase_date: {
    type: String,
    required: true,
  },
  car_make: {
    type: String,
    required: true,
  },
  car_model: {
    type: String,
    required: true,
  },
  car_year: {
    type: Number,
    required: true,
  },
});

// Export the model
module.exports = mongoose.model('reviews', reviews);
