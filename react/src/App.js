import React from 'react';
import './App.css';
import Homepage from './containers/Home'; //this container is created below

function App() {
    return (
        <div className="App">
            <Homepage /> // our imported Homepage container
        </div>
    );
}

export default App;