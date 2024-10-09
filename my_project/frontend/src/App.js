import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import Forum from './components/Forum';

function App() {
    return (
        <Router>
            <div className="container text-center">
                <h1>Welcome to the Forum</h1>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <Link className="nav-link" to="/signup">Signup</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/login">Login</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/forum">Forum</Link>
                            </li>
                        </ul>
                    </div>
                </nav>

                <Switch>
                    <Route path="/signup" component={Signup} />
                    <Route path="/login" component={Login} />
                    <Route path="/forum" component={Forum} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
