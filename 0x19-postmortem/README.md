
stmortem Report: Web Application Outage



Issue Summary:

Duration: The outage lasted 2 hours and 37 minutes, starting at 10:15 AM and ending at 12:52 PM EAT on August 12th, 2024.
Impact: During this period, the main web application service experienced severe performance degradation, causing a 75% drop in response speed and affecting 65% of users. Users reported prolonged loading times, with some requests timing out entirely, leading to a significant decrease in user engagement and several complaints on customer support channels.
Root Cause: The outage was caused by an unanticipated memory leak in a recent deployment of the backend service, which overwhelmed the application's server resources.


Timeline:

10:15 AM: Issue detected via a monitoring alert that indicated a spike in response times and memory usage.
10:20 AM: The DevOps engineer on call verified the alert and observed a 300% increase in server memory consumption.
10:25 AM: Initial assumption was that the issue was related to an external API latency, leading to the investigation of API call logs.
10:45 AM: Escalated to the backend engineering team after API logs showed normal behavior.
11:00 AM: Backend team suspected a database connection pool exhaustion due to slow query performance and initiated database monitoring.
11:25 AM: Misleading database metrics led to a delay in identifying the actual cause, as database connections were healthy.
11:40 AM: A code review of the recent deployment revealed a potential memory leak in a new caching mechanism.
12:00 PM: Engineers rolled back to the previous stable version of the application.
12:52 PM: Full service was restored, and monitoring indicated that memory usage had returned to normal levels.


Root Cause and Resolution:

The root cause of the outage was traced back to a memory leak in the newly implemented caching mechanism. The cache was not properly releasing memory when items were evicted, leading to a gradual but significant increase in memory consumption. As the memory usage approached critical levels, the server began to swap memory to disk, drastically reducing application performance and causing requests to time out.

The issue was resolved by rolling back to the previous stable version of the application, which did not include the faulty caching mechanism. Once the rollback was complete, memory usage dropped back to expected levels, and application performance returned to normal. A thorough code review and additional testing confirmed the memory leak in the new caching mechanism.



Corrective and Preventative Measures:

To prevent similar issues in the future, the following measures will be implemented:

Improve Code Review Process: Enhance the code review process with a focus on memory management, especially when introducing new caching or resource-heavy components.
Increase Testing Coverage: Implement more rigorous stress testing and memory leak detection in staging environments before deploying to production.
Monitoring Enhancements: Add monitoring specifically for memory consumption and other critical resource metrics with thresholds to trigger earlier alerts.
Actionable Tasks:
  - Refactor and patch the faulty caching mechanism to properly manage memory.
  - Update the staging environment to simulate higher load and stress conditions.
  - Implement automated memory leak detection tools as part of the CI/CD pipeline.
  - Conduct training sessions for developers on resource management best practices.

These steps will help ensure the stability and performance of the web application, reducing the likelihood of similar outages in the future.


