import React, { useState } from "react";
import "./App.css";
import axios from "axios";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';

function App() {
  const [tax, setTax] = useState("");
  const [income, setincome] = useState("");
  const getTaxValue = (event) => {
    event.preventDefault();
    axios
      .post("https://taxcalculator-k815.onrender.com/calculate/tax", {income })
      .then((response) => {
        setTax(response.data.taxvalue);
        console.log(response)
      })
      .catch((err) => {
        console.log("error", err);
      });
  };

  return (
    <div className="main flex">
      <h1>get value of tax</h1>
      <label>enter the income before tax:</label>
      <TextField id="outlined-basic" label="Outlined" variant="outlined"
        type="number"
        value={income}
        onChange={(e) => {
          setincome(e.target.value);
        }}
      />
      <Button variant="contained" onClick={getTaxValue}>get tax value</Button>
      {tax &&(
      <Alert severity="info">Tax payable: <b style={{letterSpacing:".1rem"}}>{tax}</b></Alert>)}
    </div>
  );
}

export default App;
