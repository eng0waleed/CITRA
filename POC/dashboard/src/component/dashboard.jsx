import React, { useEffect, useState } from 'react';
import { Grid, Paper, Typography } from '@mui/material';
import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

const CITRADashboard = () => {
const [chartData, setChartData] = useState({
labels: [],
datasets: [{
label: 'Emotion Distribution',
data: [],
backgroundColor: [
'rgba(255, 99, 132, 0.2)',
'rgba(54, 162, 235, 0.2)',
// ... add more colors as needed
],
borderColor: [
'rgba(255, 99, 132, 1)',
'rgba(54, 162, 235, 1)',
// ... add more border colors as needed
],
borderWidth: 1
}]
});

useEffect(() => {
fetch('https://citra-eva2ckcawq-uc.a.run.app/values') // Replace with your API endpoint
.then(response => response.json())
.then(data => {
console.log()
const emotions = Object.keys(data);
const percentages = Object.values(data);

setChartData(prevData => ({
...prevData,
labels: emotions,
datasets: [{
...prevData.datasets[0],
data: percentages
}]
}));
})
.catch(error => {
console.error('Error fetching data:', error);
// Handle error state as needed
});
}, []);

return (
<Grid container spacing={2}>
<Grid item xs={12}>
<Paper elevation={3} style={{ padding: '20px' }}>
<Typography variant="h4" gutterBottom>
CITRA Dashboard
</Typography>
{chartData.labels.length > 0 ? (
<Pie data={chartData} />
) : (
<Typography variant="subtitle1">Loading data...</Typography>
)}
</Paper>
</Grid>
</Grid>
);
};

export default CITRADashboard;

