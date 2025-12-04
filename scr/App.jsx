import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Moon, Star, Clock, Play, Pause, Volume2, VolumeX } from 'lucide-react';

const ParticleCanvas = ({ activeLights }) => {
  const canvasRef = useRef(null);
  
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
    
    const particles = [];
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        size: Math.random() * 2 + 0.5,
        speedX: (Math.random() - 0.5) * 0.5,
        speedY: (Math.random() - 0.5) * 0.5,
        opacity: Math.random() * 0.8 + 0.2
      });
    }
    
    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      particles.forEach((particle, index) => {
        particle.x += particle.speedX;
        particle.y += particle.speedY;
        
        if (particle.x < 0 || particle.x > canvas.width) particle.speedX *= -1;
        if (particle.y < 0 || particle.y > canvas.height) particle.speedY *= -1;
        
        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${particle.opacity})`;
        ctx.fill();
        
        for (let j = index + 1; j < particles.length; j++) {
          const dx = particle.x - particles[j].x;
          const dy = particle.y - particles[j].y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          
          if (distance < 100) {
            ctx.beginPath();
            ctx.moveTo(particle.x, particle.y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.strokeStyle = `rgba(255, 255, 255, ${0.1 * (1 - distance / 100)})`;
            ctx.stroke();
          }
        }
      });
      
      requestAnimationFrame(animate);
    };
    
    animate();
  }, []);
  
  return (
    <canvas 
      ref={canvasRef}
      className="particle-canvas"
      style={{ opacity: activeLights > 0 ? 1 : 0.3 }}
    />
  );
};

const LightButton = ({ position, isOn, onToggle }) => {
  return (
    <button
      className="light-btn"
      style={{
        left: `${position.x}%`,
        top: `${position.y}%`
      }}
      onClick={onToggle}
    >
      <div className={isOn ? 'light-on' : 'light-off'} />
    </button>
  );
};

function App() {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [wakeTime, setWakeTime] = useState('07:00');
  const [isSleeping, setIsSleeping] = useState(false);
  const [activeLights, setActiveLights] = useState(3);
  const [lights, setLights] = useState([
    { id: 1, x: 20, y: 25, on: true },
    { id: 2, x: 70, y: 15, on: true },
    { id: 3, x: 45, y: 40, on: true },
    { id: 4, x: 15, y: 70, on: false },
    { id: 5, x: 80, y: 60, on: false },
    { id: 6, x: 60, y: 85, on: false }
  ]);
  const [soundEnabled, setSoundEnabled] = useState(false);
  const [ambientRain, setAmbientRain] = useState(false);
  const [ambientFireplace, setAmbientFireplace] = useState(true);
  const [rainVolume, setRainVolume] = useState(60);
  const [fireplaceVolume, setFireplaceVolume] = useState(40);
  const [sleepStage, setSleepStage] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);
    
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    if (isSleeping) {
      const stages = ['Falling Asleep', 'Light Sleep', 'Deep Sleep', 'REM Sleep'];
      let stage = 0;
      
      const stageInterval = setInterval(() => {
        stage++;
        setSleepStage(stage);
        
        if (stage >= stages.length) {
          stage = 0;
        }
      }, 3000);
      
      return () => clearInterval(stageInterval);
    }
  }, [isSleeping]);

  const toggleLight = (id) => {
    setLights(lights.map(light => 
      light.id === id ? { ...light, on: !light.on } : light
    ));
    setActiveLights(lights.filter(light => light.on && light.id !== id).length + 1);
  };

  const handleSleep = () => {
    setIsSleeping(!isSleeping);
  };

  const formatTime = (date) => {
    return date.toLocaleTimeString('en-US', { 
      hour12: true, 
      hour: 'numeric', 
      minute: '2-digit',
      second: '2-digit'
    });
  };

  const formatDate = (date) => {
    return date.toLocaleDateString('en-US', { 
      weekday: 'long',
      month: 'long',
      day: 'numeric'
    });
  };

  const sleepStages = ['Falling Asleep', 'Light Sleep', 'Deep Sleep', 'REM Sleep'];

  return (
    <div className="app">
      <div className="topbar">
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <Moon size={24} />
          <h1 style={{ margin: 0, fontSize: '20px' }}>Starlight Sleepover</h1>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '14px' }}>
          <Star size={16} />
          <span>{activeLights} lights active</span>
        </div>
      </div>

      <div className="layout">
        <div className="hero">
          <div className="hero-left">
            <div style={{ marginBottom: '16px' }}>
              <h2 style={{ margin: '0 0 8px 0', fontSize: '18px' }}>Tonight's Sleep Space</h2>
              <p style={{ margin: 0, fontSize: '14px', opacity: 0.7 }}>
                Create your perfect stargazing environment
              </p>
            </div>
            
            <div className="hero-right" style={{ position: 'relative' }}>
              <img 
                src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop&crop=center"
                alt="Starry night sky"
                className="hero-img"
              />
              
              <div className="lights-overlay">
                {lights.map(light => (
                  <LightButton
                    key={light.id}
                    position={{ x: light.x, y: light.y }}
                    isOn={light.on}
                    onToggle={() => toggleLight(light.id)}
                  />
                ))}
              </div>
              
              <ParticleCanvas activeLights={activeLights} />
            </div>
            
            <div className="thumbnails" style={{ display: 'flex', marginTop: '12px' }}>
              <img 
                src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=68&h=68&fit=crop&crop=center"
                alt="Scene 1"
              />
              <img 
                src="https://images.unsplash.com/photo-1490324412500-8d7e85eab80c?w=68&h=68&fit=crop&crop=center"
                alt="Scene 2"
              />
              <img 
                src="https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=68&h=68&fit=crop&crop=center"
                alt="Scene 3"
              />
            </div>
          </div>

          <div className="sidebar">
            <div className="widget">
              <h3>
                <Clock size={16} style={{ marginRight: '8px', verticalAlign: 'middle' }} />
                Current Time
              </h3>
              <div className="clock">{formatTime(currentTime)}</div>
              <div style={{ textAlign: 'center', fontSize: '14px', opacity: 0.7 }}>
                {formatDate(currentTime)}
              </div>
              
              <div className="time-input">
                <label style={{ fontSize: '14px' }}>Wake up at:</label>
                <input 
                  type="time" 
                  value={wakeTime}
                  onChange={(e) => setWakeTime(e.target.value)}
                />
              </div>
            </div>

            <div className="widget">
              <h3>Sleep Tracker</h3>
              <div className="quick-stats">
                <div className="stat">
                  <div className="stat-value">7.2h</div>
                  <div className="stat-label">Last Night</div>
                </div>
                <div className="stat">
                  <div className="stat-value">85%</div>
                  <div className="stat-label">Sleep Quality</div>
                </div>
              </div>
              
              <button 
                className="sleep-btn"
                onClick={handleSleep}
                style={{ background: isSleeping ? '#ef4444' : '#4a9eff' }}
              >
                {isSleeping ? (
                  <>
                    <Pause size={16} style={{ marginRight: '8px' }} />
                    Wake Up
                  </>
                ) : (
                  <>
                    <Moon size={16} style={{ marginRight: '8px' }} />
                    Start Sleep Mode
                  </>
                )}
              </button>
            </div>

            <AnimatePresence>
              {isSleeping && (
                <motion.div 
                  className="widget"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -20 }}
                >
                  <h3>Sleep Stage</h3>
                  <div className="sleep-stage">
                    <div className="stage-indicator">
                      <div className="breath-circle">
                        <div className="breath-dot" />
                      </div>
                    </div>
                    <div className="stage-text">
                      {sleepStages[sleepStage]}
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            <div className="widget">
              <h3>Ambient Sounds</h3>
              <div className="sound-controls">
                <button 
                  className={`sound-btn ${soundEnabled ? 'active' : ''}`}
                  onClick={() => setSoundEnabled(!soundEnabled)}
                >
                  {soundEnabled ? <Volume2 size={16} /> : <VolumeX size={16} />}
                  <div style={{ fontSize: '12px', marginTop: '4px' }}>
                    {soundEnabled ? 'On' : 'Off'}
                  </div>
                </button>
              </div>
              
              <AnimatePresence>
                {soundEnabled && (
                  <motion.div 
                    className="ambient-controls"
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    exit={{ opacity: 0, height: 0 }}
                  >
                    <div className="ambient-item">
                      <div className="ambient-label">Rain</div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <div className={`ambient-toggle ${ambientRain ? 'active' : ''}`} onClick={() => setAmbientRain(!ambientRain)}>
                          <div className="ambient-toggle-dot" />
                        </div>
                        <input 
                          type="range" 
                          min="0" 
                          max="100" 
                          value={rainVolume}
                          onChange={(e) => setRainVolume(e.target.value)}
                          className="ambient-slider"
                          style={{ width: '60px' }}
                        />
                      </div>
                    </div>
                    
                    <div className="ambient-item">
                      <div className="ambient-label">Fireplace</div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <div className={`ambient-toggle ${ambientFireplace ? 'active' : ''}`} onClick={() => setAmbientFireplace(!ambientFireplace)}>
                          <div className="ambient-toggle-dot" />
                        </div>
                        <input 
                          type="range" 
                          min="0" 
                          max="100" 
                          value={fireplaceVolume}
                          onChange={(e) => setFireplaceVolume(e.target.value)}
                          className="ambient-slider"
                          style={{ width: '60px' }}
                        />
                      </div>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;