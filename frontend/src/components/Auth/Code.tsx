import React from 'react';

import instance from '../../api';

const AuthCode = () => {
  const [code, setCode] = React.useState('');
  const [show, setShow] = React.useState(false);

  const handleClick = async () => {
    const response = await instance.post('/staff/code');
  };

  return (
    <div className='container'>
      <h1>AuthCode page</h1>

      <button type='button' className='btn btn-outline-primary' onClick={handleClick}>
        Generate Authorization Code
      </button>
    </div>
  );
};

export default AuthCode;
