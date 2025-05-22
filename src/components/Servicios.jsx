import React from 'react';
import {
  Box,
  Grid,
  Typography,
  Card,
  CardActionArea,
  CardContent,
  Stack,
} from '@mui/material';

import SearchIcon from '@mui/icons-material/Search';
import BarChartIcon from '@mui/icons-material/BarChart';
import LightbulbIcon from '@mui/icons-material/Lightbulb';
import EngineeringIcon from '@mui/icons-material/Engineering';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import AssessmentIcon from '@mui/icons-material/Assessment';

const servicios = [
  {
    titulo: 'Servicios Energéticos',
    subtitulo: 'Energy Services',
    items: [
      {
        icon: <SearchIcon sx={{ fontSize: 50 }} color="primary" />,
        textoEs: 'Auditorías Energéticas',
        textoEn: 'Energy Audits',
        link: '#',
      },
      {
        icon: <BarChartIcon sx={{ fontSize: 50 }} color="primary" />,
        textoEs: 'Optimización de Potencia Contratada',
        textoEn: 'Power Optimization',
        link: '#',
      },
      {
        icon: <LightbulbIcon sx={{ fontSize: 50 }} color="primary" />,
        textoEs: 'Eficiencia Energética',
        textoEn: 'Energy Efficiency',
        link: '#',
      },
      {
        icon: <EngineeringIcon sx={{ fontSize: 50 }} color="primary" />,
        textoEs: 'Diseño de Medidas de Ahorro',
        textoEn: 'Efficiency Measures Design',
        link: '#',
      },
      {
        icon: <ManageAccountsIcon sx={{ fontSize: 50 }} color="primary" />,
        textoEs: 'Gestión Energética Integral',
        textoEn: 'Energy Management',
        link: '#',
      },
      {
        icon: <AssessmentIcon sx={{ fontSize: 50 }} color="primary" />,
        textoEs: 'Monitoreo y Análisis del Consumo',
        textoEn: 'Energy Monitoring & Analysis',
        link: '#',
      },
    ],
  },
];

export default function Servicios() {
  return (
    <Box sx={{ p: { xs: 2, md: 4 } }}>
      <Typography variant="h4" gutterBottom color="primary" sx={{ fontWeight: 600 }}>
        Servicios
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        Auditoría, Optimización y Gestión Energética
      </Typography>

      <Grid container spacing={4}>
        {servicios.map((bloque, index) => (
          <Grid item xs={12} key={index}>
            <Typography variant="h5" color="secondary" gutterBottom sx={{ fontWeight: 500 }}>
              {bloque.titulo}
            </Typography>
            <Typography variant="body2" color="text.secondary" gutterBottom sx={{ mb: 2 }}>
              {bloque.subtitulo}
            </Typography>

            <Grid container spacing={2}>
              {bloque.items.map((item, idx) => (
                <Grid item xs={12} sm={6} md={4} key={idx}>
                  <Card elevation={3} sx={{ height: '100%' }}>
                    <CardActionArea href={item.link} sx={{ height: '100%' }}>
                      <CardContent>
                        <Stack spacing={1.5} alignItems="center" justifyContent="center">
                          {item.icon}
                          <Typography variant="body1" align="center" sx={{ fontWeight: 500 }}>
                            {item.textoEs}
                          </Typography>
                          <Typography variant="body2" align="center" color="text.secondary">
                            {item.textoEn}
                          </Typography>
                        </Stack>
                      </CardContent>
                    </CardActionArea>
                  </Card>
                </Grid>
              ))}
            </Grid>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}
