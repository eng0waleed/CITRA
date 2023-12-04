import React, { useEffect, useState } from 'react';
import { Grid, Paper, Typography } from '@mui/material';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

const CITRADashboard = () => {
  const [chartData, setChartData] = useState({ datasets: [] });

  useEffect(() => {
    fetch('https://citra-eva2ckcawq-uc.a.run.app/values')
      .then(response => response.json())
      .then(data => {
        setChartData({
          labels: Object.keys(data),
          datasets: [{
            label: 'Emotion Distribution',
            data: Object.values(data),
            backgroundColor: [
              '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
            ],
            borderColor: [
              '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
            ],
            borderWidth: 1
          }]
        });
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <Grid container spacing={2} justifyContent="center" alignItems="center" style={{ height: '100vh' }}>
      <Grid item style={{ width: '50vw', height: '50vh' }}>
        <Paper elevation={3} style={{ padding: '50px', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          <Typography variant="h4" gutterBottom style={{ textAlign: 'center' }}>
            CITRA Dashboard
          </Typography>
          {chartData.datasets.length > 0 ? (
            <Pie data={chartData} />
          ) : (
            <Typography variant="subtitle1" style={{ textAlign: 'center' }}>Loading data...</Typography>
          )}
        </Paper>
      </Grid>
    </Grid>
  );
};

export default CITRADashboard;
