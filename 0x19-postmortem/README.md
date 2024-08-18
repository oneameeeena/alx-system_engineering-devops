The Spaghetti Saga: DineDash’s Unexpected Viral Frenzy
Issue Summary:

On August 18, 2024, from 19:00 to 21:15 PDT, DineDash’s food delivery platform suffered a major service disruption. During this time, 88% of our customers were unable to place orders, browse restaurant options, or track deliveries. The root cause was traced back to a database bottleneck triggered by an unexpected 600% spike in traffic due to a viral TikTok challenge that encouraged users to create the “most complicated order” using our app.

Timeline:

19:00 PDT: Traffic surge detected by our monitoring systems.
19:02 PDT: On-call engineer received alert for high database load.
19:05 PDT: Initial investigation focused on potential bot activity.
19:10 PDT: Security team ruled out external attacks.
19:25 PDT: Database team identified an unusually high number of long-running queries.
19:35 PDT: Social media team flagged a viral TikTok trend involving DineDash.
19:45 PDT: Incident escalated to the senior engineering team and CTO.
20:10 PDT: Root cause identified as database query overload due to complex orders.
20:30 PDT: Emergency patch deployed to optimize database queries.
21:15 PDT: Systems fully restored and normal service resumed.
Root Cause and Resolution:

The outage was caused by an unforeseen surge in traffic due to a viral TikTok challenge where users competed to create the most intricate and large orders, overwhelming our database with complex queries. Our database was optimized for typical peak loads but not for this extraordinary and concentrated increase in activity.
To resolve the issue, we deployed an emergency patch that optimized query processing and temporarily disabled certain complex order features. We also implemented a dynamic scaling solution for our database infrastructure to handle similar future events.

Corrective and Preventative Measures:

1. Infrastructure Scaling:

TODO: Implement dynamic scaling for database resources.
TODO: Upgrade database infrastructure to manage 5x the current peak load.
2. Monitoring and Alerting:

TODO: Add alerts specifically for long-running database queries.
TODO: Implement real-time monitoring of social media trends for proactive scaling.
3. Code Optimization:

TODO: Optimize query processing for complex orders.
TODO: Implement a caching layer for frequently accessed data.
4. Incident Response:

TODO: Develop a playbook for handling sudden viral-driven traffic spikes.
TODO: Conduct regular load testing to simulate extreme traffic conditions.
5. Communication:

TODO: Enhance our status page to provide detailed updates during outages.
TODO: Implement an automated system to issue apologies and coupons to affected users.
Conclusion:

While the “Spaghetti Saga” momentarily tangled up our system, we’ve learned valuable lessons about the unpredictability of social media-driven traffic. We’re rapidly implementing improvements to ensure DineDash can handle the unexpected with ease. In the meantime, keep placing those orders, and remember—we’re always here to deliver, no matter how complex the dish!

Keep calm and DineDash on. We’ve got your cravings covered!
