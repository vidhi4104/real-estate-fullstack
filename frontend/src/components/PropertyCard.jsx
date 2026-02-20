import React from 'react';

const PropertyCard = ({ property }) => {
  const imageUrl = `http://13.232.29.33:5000${property.image_url}`;


  return (
    <div className="property-card">
      <img
        src={imageUrl}
        alt={property.title}
        style={{ width: "100%", height: "220px", objectFit: "cover" }}
      />

      <div className="property-info">
        <h3>{property.title}</h3>
        <p>{property.location}</p>
        <h4>₹ {property.price}</h4>
      </div>
    </div>
  );
};

export default PropertyCard;
