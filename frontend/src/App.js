import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function App() {
  const [page, setPage] = useState('login');
  const [token, setToken] = useState(null);
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Check if token exists on mount
  useEffect(() => {
    const savedToken = localStorage.getItem('access_token');
    if (savedToken) {
      setToken(savedToken);
      fetchCurrentUser(savedToken);
    } else {
      setLoading(false);
    }
  }, []);

  const fetchCurrentUser = async (accessToken) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/users/me`, {
        headers: { Authorization: `Bearer ${accessToken}` },
      });
      setCurrentUser(response.data);
      setPage('dashboard');
      setLoading(false);
    } catch (error) {
      console.error('Failed to fetch current user:', error);
      localStorage.removeItem('access_token');
      setToken(null);
      setLoading(false);
    }
  };

  const handleLoginSuccess = (accessToken, user) => {
    localStorage.setItem('access_token', accessToken);
    setToken(accessToken);
    setCurrentUser(user);
    setPage('dashboard');
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    setToken(null);
    setCurrentUser(null);
    setPage('login');
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (!token) {
    return (
      <>
        {page === 'login' ? (
          <Login
            onLoginSuccess={handleLoginSuccess}
            onSwitchToRegister={() => setPage('register')}
          />
        ) : (
          <Register
            onRegisterSuccess={handleLoginSuccess}
            onSwitchToLogin={() => setPage('login')}
          />
        )}
      </>
    );
  }

  return (
    <>
      <nav>
        <h1>📋 Task Manager</h1>
        <div className="nav-right">
          <span id="userInfo">{currentUser?.email}</span>
          <button className="logoutBtn" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </nav>
      <Dashboard token={token} />
    </>
  );
}

export default App;
