-- select username, email
-- from users
-- where created_at < '2015-01-01' and
-- created_at > '2013-01-01' and 
-- email is not null;

-- select user_id, count(id)
-- from posts
-- group by user_id
-- order by count(id) desc;

-- select extract(month from created_at) as join_month, 
-- 	count(*) as user_count
-- from users
-- group by join_month
-- order by user_count desc
-- limit 1;

-- select avg(length(caption)) from posts;

-- select length(caption) as cap_length 
-- from posts
-- where caption is not null
-- order by cap_length desc
-- limit 5;

-- select user_id, count(id) as posts
-- from posts
-- group by user_id
-- having count(id) = 8;