import React, { Component } from 'react'
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import CircularProgress from '@material-ui/core/CircularProgress'
import Select from '@material-ui/core/Select'
import MenuItem from '@material-ui/core/MenuItem'
import InputLabel from '@material-ui/core/InputLabel'
import FormControl from '@material-ui/core/FormControl'
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextareaAutosize from '@material-ui/core/TextareaAutosize'
import JokeTable from './joke-table'
import api from '../api'

export default class JokesPanel extends Component {

  constructor(props) {
    super(props)
    this.state = {
      jokes: [],
      loading: false,
      query: '',
      queryError: false,
      page: 0,
      searchBy: 'text',
      newJokeText: '',
      createJokeDialogOpen: false
    }
  }

  setPage = page => this.setState({ page })

  onSearch = () => {
    if(this.state.query === '') {
      this.setState({queryError: true})
    } else {
      this.setState({queryError: false})
      this.setState({loading: true})

      if(this.state.searchBy === 'text') {
        api.get_jokes_by_query(
          this.state.query,
          res => this.setState({jokes: res.data['jokes'], loading: false, page: 0})
        )
      } else {
        api.getJokeByID(
          this.state.query,
          res => this.setState({jokes: [res.data], loading: false, page: 0}),
          res => this.setState({jokes: [], loading: false, page: 0})
        )
      }
    }
   }

  keyPress = e => {
    if(e.key === 'Enter') {
      this.onSearch()
    }
  }

  deleteJoke = id => {
    this.setState({loading: true})
    api.delete_joke_by_id(
      id,
      () => {
        const newJokes = this.state.jokes.filter(joke => joke.id !== id)
        this.setState({ jokes: newJokes, loading: false })
      }
    )
  }

  editJoke = (id, text) => {
    this.setState({loading: true})
    api.editJokeById(
      id,
      text,
      () => {
        const newJokes = this.state.jokes.map(joke => (joke.id === id) ? { id, text } : joke)
        this.setState({ jokes: newJokes, loading: false })
      }
    )
  }

  handleJokeSubmit = _event => {
    this.setState({loading: true, createJokeDialogOpen: false})
    api.createJoke(
      this.state.newJokeText,
      (res) => {
        this.setState({jokes: [res.data], loading: false, page:0, newJokeText: ''})
      }
    )
  }

  render() {
    return(<div style={{marginLeft: '5vw', marginRight: '5vw'}}>
        <Grid container spacing={3} style={{marginTop: 10}}>
          <Grid item xs={6}>
          <TextField
            id="filled-search"
            label="Search field"
            type="search"
            variant="outlined" 
            fullWidth
            value={this.state.query}
            onChange={(event) => this.setState({query: event.target.value})}
            error={this.state.queryError}
            helperText={this.state.queryError ? 'Please enter a query to search' : ''}
            onKeyPress={this.keyPress}
          />
          </Grid>
          <Grid item xs={3}>
            <FormControl style={{minWidth: '100%'}}>
              <InputLabel id="typeOfSearchLabel">Search by</InputLabel>
              <Select
                labelId="typeOfSearchLabel"
                id="typeOfSearch"
                value={this.state.searchBy}
                onChange={(event) => this.setState({searchBy: event.target.value})}
                label="Search by"
              >
                <MenuItem value={'text'}>text</MenuItem>
                <MenuItem value={'id'}>id</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={3}>
            <Button
              variant="contained"
              fullWidth
              style={{lineHeight: '40px', backgroundColor: '#52a27c'}}
              onClick={this.onSearch}
            >
              Search
            </Button>
          </Grid>
          <Grid item xs={12}>
            {
              this.state.loading ?
                <CircularProgress />
              :
                <JokeTable
                  jokes={this.state.jokes}
                  deleteJoke={this.deleteJoke}
                  editJoke={this.editJoke}
                  page={this.state.page}
                  setPage={this.setPage}
                />
            }
          </Grid>
        </Grid>
        <Fab
          color="primary"
          aria-label="add"
          style={{position: 'fixed', right: '15px', bottom: '20px', backgroundColor: '#52a27c'}}
          onClick={() => this.setState({createJokeDialogOpen: true})}
        >
          <AddIcon />
        </Fab>
        <Dialog 
          open={this.state.createJokeDialogOpen}
          onClose={() => this.setState({createJokeDialogOpen: false})}
          aria-labelledby="create-dialog-title"
          fullWidth
          >
          <DialogTitle id="create-dialog-title">Create joke</DialogTitle>
          <DialogContent>
            <TextareaAutosize
              aria-label="empty textarea"
              placeholder="Enter joke"
              autoFocus
              margin="dense"
              id="createJoke"
              label="new joke"
              type="textarea"
              value={this.state.newJokeText}
              onChange={(event) => this.setState({newJokeText: event.target.value})}
              cols={60}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleJokeSubmit} color="primary">
              Create
            </Button>
          </DialogActions>
        </Dialog>
      </div>)
  }
}