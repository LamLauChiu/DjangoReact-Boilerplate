import React, { Component  } from "react";
import ReactDOM from "react-dom";

class App extends Component {
    render() {
        return (
            <div>
               <h2>Content</h2>
               <p>The content text!!!</p>
            </div>
         );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));