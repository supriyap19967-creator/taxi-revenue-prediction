-- =====================================================
-- Analytics view: enrich trips with time-based features
-- =====================================================
CREATE VIEW final_taxi_analytics AS
SELECT
    trip_id,
    CAST(strftime('%H', tpep_pickup_datetime) AS INTEGER) AS pickup_hour,
    CAST(strftime('%w', tpep_pickup_datetime) AS INTEGER) AS pickup_weekday,
    trip_distance,
    passenger_count,
    fare_amount,
    tip_amount,
    total_amount,
    payment_type,
    (julianday(tpep_dropoff_datetime) - julianday(tpep_pickup_datetime)) * 24 * 60
        AS trip_duration_minutes
FROM trips;


-- =====================================================
-- ML-ready aggregated features (used for model training)
-- =====================================================
CREATE VIEW final_taxi_ml_ready AS
SELECT
    pickup_hour,
    pickup_weekday,
    payment_type,

    COUNT(trip_id)                       AS trip_count,
    AVG(trip_distance)                   AS avg_trip_distance,
    AVG(trip_duration_minutes)           AS avg_trip_duration,
    AVG(fare_amount)                     AS avg_fare_amount,
    AVG(tip_amount)                      AS avg_tip_amount,
    SUM(total_amount)                    AS total_revenue

FROM final_taxi_analytics
GROUP BY
    pickup_hour,
    pickup_weekday,
    payment_type;


-- =====================================================
-- Optional: aggregated metrics view for analysis
-- =====================================================
CREATE VIEW taxi_aggregated_metrics AS
SELECT
    pickup_hour,
    pickup_weekday,
    payment_type,

    COUNT(trip_id)        AS trip_count,
    SUM(total_amount)     AS total_revenue,
    AVG(fare_amount)      AS avg_fare_amount,
    AVG(tip_amount)       AS avg_tip_amount

FROM final_taxi_analytics
GROUP BY
    pickup_hour,
    pickup_weekday,
    payment_type;
