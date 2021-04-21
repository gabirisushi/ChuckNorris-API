import './App.css';
import AppBar from '@material-ui/core/AppBar'
import Typography from '@material-ui/core/Typography'
import JokesPanel from './components/jokes-panel'

function App() {
  return (
    <div className="App">
      <AppBar position='static' style={{height: 50, backgroundColor: '#00628B'}}>
        <Typography variant="h6" style={{lineHeight: '50px'}}>
          Joke API
        </Typography>
      </AppBar>
      <JokesPanel />
    </div>
  )
}

export default App;
