import React from 'react';
import Login from './components/Login';
import Signup from './components/Signup';
import Forum from './components/Forum';

function App() {
    return (
        <div>
            <h1>Welcome to the Forum</h1>
            <Signup />
            <Login />
            <Forum />
        </div>
    );
}

export default App;
