import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function Dashboard({ token }) {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchTasks();
  }, [token]);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_BASE_URL}/tasks`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      console.log('Fetched tasks:', response);
      if(response.data && response.data.tasks) {
        setTasks(response.data.tasks);
      } else {
        setTasks([]);
      }
      setError('');
    } catch (err) {
      setError('Failed to fetch tasks');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (e) => {
    e.preventDefault();
    if (!newTask.trim()) return;

    try {
      const response = await axios.post(
        `${API_BASE_URL}/tasks`,
        { title: newTask },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setTasks([...tasks, response.data]);
      setNewTask('');
      setError('');
    } catch (err) {
      setError('Failed to create task');
      console.error(err);
    }
  };

  const handleToggleTask = async (taskId, completed) => {
    try {
      const response = await axios.put(
        `${API_BASE_URL}/tasks/${taskId}`,
        { completed: !completed },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setTasks(tasks.map((t) => (t.id === taskId ? response.data : t)));
      setError('');
    } catch (err) {
      setError('Failed to update task');
      console.error(err);
    }
  };

  const handleDeleteTask = async (taskId) => {
    try {
      await axios.delete(`${API_BASE_URL}/tasks/${taskId}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setTasks(tasks.filter((t) => t.id !== taskId));
      setError('');
    } catch (err) {
      setError('Failed to delete task');
      console.error(err);
    }
  };

  if (loading) {
    return <div className="loading">Loading tasks...</div>;
  }

  return (
    <div className="dashboard">
      {error && <div className="msg error">{error}</div>}

      <div className="card">
        <h3>Create New Task</h3>
        <form onSubmit={handleCreateTask} className="create-row">
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="What do you need to do?"
          />
          <button type="submit" className="btn">
            Add Task
          </button>
        </form>
      </div>

      <div className="card">
        <h3>My Tasks</h3>
        {tasks && tasks.length > 0 ? (
          <ul className="tasks-list">
            {tasks.map((task) => (
              <li key={task.id} className="task-item">
                <div className="task-content">
                  <input
                    type="checkbox"
                    className="task-checkbox"
                    checked={task.completed || false}
                    onChange={() => handleToggleTask(task.id, task.completed)}
                  />
                  <span
                    className={`task-text ${task.completed ? 'completed' : ''}`}
                  >
                    {task.title}
                  </span>
                </div>
                <div className="task-actions">
                  <button
                    className="task-btn"
                    onClick={() => handleDeleteTask(task.id)}
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        ) : (
          <div className="empty-state">
            <p>No tasks yet. Create one to get started!</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;
