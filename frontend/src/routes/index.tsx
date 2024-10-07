import { createBrowserRouter } from 'react-router-dom';
import { Staff, StaffList, Login, Register, AuthCode, Home, NotFound } from '../components';

const routes = [
  {
    path: '/code',
    element: <AuthCode />,
  },
  {
    path: '/auth',
    children: [
      {
        path: 'login',
        element: <Login />,
      },
      {
        path: 'register',
        element: <Register />,
      },
    ],
  },
  {
    path: '/staff',
    children: [
      {
        path: '',
        element: <StaffList />,
      },
      {
        path: ':employee_no',
        element: <Staff />,
      },
    ],
  },
];

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
    errorElement: <NotFound />,
  },
  ...routes,
]);

export default router;
