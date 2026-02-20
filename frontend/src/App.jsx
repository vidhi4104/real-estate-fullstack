import axios from "axios";

import React from 'react';
import { useEffect, useState } from "react";

import Navbar from './components/Navbar';
import Footer from './components/Footer';
import PropertyCard from './components/PropertyCard';


function App() {

  const [properties, setProperties] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/properties")
      .then((res) => {
        setProperties(res.data);
      })
      .catch((err) => console.log(err));

  }, []);





  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };



  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Message sent successfully!');
    e.target.reset();
  };

  return (
    <div className="app">
      <Navbar scrollToSection={scrollToSection} />

      {/* Hero Section */}
      <section id="home" className="hero">
        <div className="hero-overlay">
          <div className="hero-content">
            <h1>Find Your Dream Home</h1>
            <p>Buy, rent and sell properties easily</p>
            <button className="btn-primary" onClick={() => scrollToSection('properties')}>
              View Properties
            </button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features">
        <div className="container">
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">👥</div>
              <h3>Trusted Agents</h3>
              <p>Work with certified and experienced real estate professionals</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">💰</div>
              <h3>Affordable Prices</h3>
              <p>Find properties that fit your budget without compromising quality</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🕐</div>
              <h3>24/7 Support</h3>
              <p>Our team is always available to assist you with any questions</p>
            </div>
          </div>
        </div>
      </section>

      {/* Properties Section */}
      <section id="properties" className="properties">
        <div className="container">
          <h2 className="section-title">Featured Properties</h2>
          <div className="properties-grid">
            {properties.map((property) => (
              <PropertyCard key={property.id} property={property} />
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="contact">
        <div className="container">
          <h2 className="section-title">Get In Touch</h2>
          <form className="contact-form" onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Your Name"
              required
              className="form-input"
            />
            <input
              type="email"
              placeholder="Your Email"
              required
              className="form-input"
            />
            <textarea
              placeholder="Your Message"
              required
              rows="5"
              className="form-input"
            ></textarea>
            <button type="submit" className="btn-primary">Submit</button>
          </form>
        </div>
      </section>

      <Footer />
    </div>
  );
}

export default App;