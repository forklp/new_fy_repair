from django.db import models

# Create your models here.
class FyAdmin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'fy_admin'


class FyComputer(models.Model):
    computer_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    buy_time = models.IntegerField()
    time = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'fy_computer'


class FyConfig(models.Model):
    key = models.CharField(unique=True, max_length=50)
    value = models.TextField()

    class Meta:
        managed = True
        db_table = 'fy_config'


class FyOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    number = models.CharField(unique=True, max_length=16)
    user_id = models.IntegerField()
    staff_id = models.IntegerField()
    time = models.IntegerField()
    status = models.IntegerField()
    vip = models.IntegerField()
    user_confirm_time = models.IntegerField()
    staff_confirm_time = models.IntegerField()
    distribute_time = models.IntegerField()
    computer_id = models.IntegerField()
    mode = models.IntegerField()
    refuse_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fy_order'


class FyOrderextend(models.Model):
    orderextend_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = True
        db_table = 'fy_orderextend'


class FyRefuse(models.Model):
    staff_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fy_refuse'


class FyRepairlog(models.Model):
    repairlog_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    staff_id = models.IntegerField()
    time = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'fy_repairlog'


class FySet(models.Model):
    week_max = models.IntegerField(blank=True, null=True)
    staff_month_refuse_max = models.IntegerField(blank=True, null=True)
    staff_day_max = models.IntegerField(blank=True, null=True)
    order_confirm_accept_max = models.IntegerField(blank=True, null=True)
    order_confirm_complete_max = models.IntegerField(blank=True, null=True)
    order_refuse_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fy_set'


class FyStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64)
    user_id = models.IntegerField()
    status = models.IntegerField()
    max = models.IntegerField()
    available = models.IntegerField()
    last_time = models.IntegerField()
    refuse_order_id = models.IntegerField()
    month_refuse_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fy_staff'


class FyUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    weixin_key = models.CharField(max_length=64)
    ucid = models.CharField(unique=True, max_length=32)
    type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'fy_user'


class FyUserextend(models.Model):
    userextend_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    register_time = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'fy_userextend'


class FyWxpush(models.Model):
    id = models.IntegerField(primary_key=True)
    openid = models.CharField(unique=True, max_length=50)
    formid = models.CharField(max_length=50)
    expire_time = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'fy_wxpush'


class FyWxuser(models.Model):
    user_id = models.CharField(unique=True, max_length=50)
    openid = models.CharField(unique=True, max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'fy_wxuser'