# STEP 10 — FULL CONTENT CALENDAR + SOCIAL PUBLISHING SYSTEM

## OVERVIEW
Build a full-scale content distribution and social publishing engine.

This system includes:
- Content calendar
- Campaign planner
- Social scheduler
- Publishing queue
- Social integrations
- Metrics dashboard
- Social media size chart system

---

## OBJECTIVE

Plan → Schedule → Publish → Track → Optimize → Scale

---

## TASK LIST

T-166 Create content calendar schema  
T-167 Create social integrations schema  
T-168 Create campaign schema  
T-169 Build calendar backend routes  
T-170 Build social account routes  
T-171 Build social post scheduler  
T-172 Build campaign planner  
T-173 Build content calendar page  
T-174 Build publishing queue  
T-175 Build social metrics dashboard  
T-176 Add social provider modules  
T-177 Add social integration docs  
T-178 Run social publishing review  

---

## DATABASE SCHEMA

### content_calendar

id  
title  
content_type  
campaign_id  
platform  
status  
scheduled_at  
published_at  
assigned_to  
priority  
notes  

---

### social_accounts

id  
platform  
account_name  
account_handle  
auth_type  
access_token  
refresh_token  
webhook_url  
status  

---

### social_posts

id  
platform  
account_id  
content_id  
campaign_id  
caption  
media_url  
status  
scheduled_at  
published_at  
metrics  

---

### campaigns

id  
name  
goal  
budget  
start_date  
end_date  
status  
platforms  
cta  

---

## BACKEND ROUTES

/api/content-calendar  
/api/content-calendar/schedule  
/api/content-calendar/publish  

/api/social/accounts  
/api/social/posts  
/api/social/posts/schedule  
/api/social/posts/publish  
/api/social/metrics  

/api/campaigns  
/api/campaigns/{id}  

---

## FRONTEND PAGES

/admin/content-calendar  
/admin/social-scheduler  
/admin/campaigns  
/admin/publishing-queue  
/admin/social-metrics  
/admin/social-size-chart  

---

## CONTENT CALENDAR FEATURES

- Drag and drop scheduling  
- Multi-platform assignment  
- Campaign linking  
- Priority tagging  
- Status tracking  

---

## SOCIAL SCHEDULER FEATURES

- Platform selector  
- Caption editor  
- Media uploader  
- Hashtag manager  
- Time scheduling  
- Preview per platform  

---

## PUBLISHING QUEUE

States:
- Draft  
- Scheduled  
- Ready  
- Publishing  
- Published  
- Failed  

---

## SOCIAL INTEGRATIONS

Platforms supported:

X / Twitter  
Instagram  
Facebook  
TikTok  
YouTube  
Reddit  
Bluesky  
Threads  
Mastodon  
Discord  
LinkedIn  
Pinterest  

---

## SOCIAL PROVIDER MODULES

Each provider must support:

connect_account  
schedule_post  
publish_post  
fetch_metrics  
handle_webhook  

---

## SOCIAL METRICS

Impressions  
Clicks  
Likes  
Shares  
Comments  
CTR  
Follower Growth  

---

## SOCIAL MEDIA SIZE CHART

### Universal Sizes

Square — 1080x1080  
Landscape — 1200x628  
Vertical — 1080x1350  
Story — 1080x1920  
Thumbnail — 1280x720  

---

### Platform Sizes

Instagram — 1080x1080 / 1080x1350  
Facebook — 1200x630  
X — 1200x675  
TikTok — 1080x1920  
YouTube — 1280x720  
LinkedIn — 1200x627  
Pinterest — 1000x1500  
Bluesky — 1200x627  
Threads — 1080x1350  
Mastodon — 1200x675  
Discord — 1200x628  

---

## WORKFLOW

1. Create content  
2. Assign campaign  
3. Select platforms  
4. Apply sizing  
5. Add caption  
6. Schedule  
7. Publish  
8. Track metrics  
9. Optimize  

---

## ADMIN DASHBOARD

Calendar View  
Campaign View  
Scheduler  
Publishing Queue  
Metrics Dashboard  
Size Chart  

---

## FILE STRUCTURE

backend/app/content_calendar  
backend/app/social_integrations  
backend/app/campaigns  

frontend/src/admin/content-calendar  
frontend/src/admin/social  
frontend/src/admin/campaigns  

docs/step-10  

---

## COMPLETION CHECKLIST

[ ] Calendar system working  
[ ] Scheduler working  
[ ] Campaign system working  
[ ] Queue system working  
[ ] Social integrations connected  
[ ] Metrics dashboard live  
[ ] Size chart implemented  

---

## COMPLETION STANDARD

System must:

Plan content  
Schedule posts  
Publish automatically  
Track performance  
Support multiple platforms  
Scale campaigns  
