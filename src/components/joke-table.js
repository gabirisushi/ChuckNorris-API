import React from 'react'
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import TablePagination from '@material-ui/core/TablePagination'
import { Button } from '@material-ui/core';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField'
import TextareaAutosize from '@material-ui/core/TextareaAutosize'

const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const StyledTableRow = withStyles((theme) => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

const useStyles = makeStyles({
  table: {
    minWidth: 700,
  },
});

export default function JokeTable(props) {
  const classes = useStyles();

  const [open, setOpen] = React.useState(false);
  const [editText, setEditText] = React.useState('')
  const [editingJokeId, setEditingJokeId] = React.useState(null)

  const handleClickOpen = joke => {
    setEditingJokeId(joke.id)
    setEditText(joke.text)
    setOpen(true)
  };

  const handleEditSubmit = () => {
    props.editJoke(editingJokeId, editText)
  }

  const handleClose = () => {
    setOpen(false);
  };

  return (<div>
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="customized table">
        <TableHead>
          <TableRow>
            <StyledTableCell align="left">ID</StyledTableCell>
            <StyledTableCell>Joke</StyledTableCell>
            <StyledTableCell></StyledTableCell>
            <StyledTableCell></StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {props.jokes.slice(props.page*9, props.page*9 + 9).map((joke) => (
            <StyledTableRow key={joke.id}>
              <StyledTableCell align="left">{joke.id}</StyledTableCell>
              <StyledTableCell component="th" scope="row">
                {joke.text}
              </StyledTableCell>
              <StyledTableCell component="td" scope="row">
                <Button style={{color: '#81A594'}} onClick={() => handleClickOpen(joke)}>Edit</Button>
              </StyledTableCell>
              <StyledTableCell component="td" scope="row">
                <Button style={{color: 'red'}} onClick={() => props.deleteJoke(joke.id)}>delete</Button>
              </StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    <TablePagination
      rowsPerPageOptions={[]}
      component="div"
      count={props.jokes.length}
      rowsPerPage={20}
      page={props.page}
      onChangePage={(_event, newPage) => props.setPage(newPage)}
    />

    <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title" fullWidth>
      <DialogTitle id="form-dialog-title">Edit joke</DialogTitle>
      <DialogContent>
        <TextareaAutosize
          aria-label="empty textarea"
          placeholder="Empty"
          autoFocus
          margin="dense"
          id="editText"
          label="Modified joke"
          type="textarea"
          value={editText}
          onChange={(event) => setEditText(event.target.value)}
          cols={60}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={handleEditSubmit} color="primary">
          Save
        </Button>
      </DialogActions>
    </Dialog>
  </div>
  );
}