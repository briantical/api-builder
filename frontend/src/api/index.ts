import axios from 'axios';

const instance = axios.create({
  baseURL: `${process.env.REACT_APP_API_URL}/api` || 'http://localhost:8000/api',
  timeout: 1000,
});

export default instance;
