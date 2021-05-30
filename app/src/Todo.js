import axios from 'axios';
import React from 'react';

const Todo = ({ title, date, description, user }) => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center' }}>
      <div style={{ width: '500px' }}>
        <p>
          <span style={{ fontWeight: 'bold' }}>{title}</span>
          {description}
        </p>
      </div>
    </div>
  );
};
