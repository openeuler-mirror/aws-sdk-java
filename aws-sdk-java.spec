Name:          aws-sdk-java
Version:       1.11.3
Release:       7
Summary:       AWS SDK for Java
License:       ASL 2.0
URL:           http://aws.amazon.com/sdk-for-java/
Source0:       https://github.com/aws/aws-sdk-java/archive/9883b981ab5103cc6944fbf8f3b973994777350f/%{name}-9883b981ab5103cc6944fbf8f3b973994777350f.tar.gz
BuildArch:     noarch

BuildRequires: maven-local, mvn(com.fasterxml.jackson.core:jackson-databind), mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires: mvn(commons-logging:commons-logging), mvn(javax.mail:javax.mail-api), mvn(joda-time:joda-time), mvn(junit:junit)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
Provides:      %{name}-acm%{?_isa} %{name}-acm
Obsoletes:     %{name}-acm
Provides:      %{name}-api-gateway%{?_isa} %{name}-api-gateway
Obsoletes:     %{name}-api-gateway
Provides:      %{name}-applicationautoscaling%{?_isa} %{name}-applicationautoscaling
Obsoletes:     %{name}-applicationautoscaling
Provides:      %{name}-autoscaling%{?_isa} %{name}-autoscaling
Obsoletes:     %{name}-autoscaling
Provides:      %{name}-bom%{?_isa} %{name}-bom
Obsoletes:     %{name}-bom
Provides:      %{name}-cloudformation%{?_isa} %{name}-cloudformation
Obsoletes:     %{name}-cloudformation
Provides:      %{name}-cloudfront%{?_isa} %{name}-cloudfront
Obsoletes:     %{name}-cloudfront
Provides:      %{name}-cloudhsm%{?_isa} %{name}-cloudhsm
Obsoletes:     %{name}-cloudhsm
Provides:      %{name}-cloudsearch%{?_isa} %{name}-cloudsearch
Obsoletes:     %{name}-cloudsearch
Provides:      %{name}-cloudtrail%{?_isa} %{name}-cloudtrail
Obsoletes:     %{name}-cloudtrail
Provides:      %{name}-cloudwatch%{?_isa} %{name}-cloudwatch
Obsoletes:     %{name}-cloudwatch
Provides:      %{name}-cloudwatchmetrics%{?_isa} %{name}-cloudwatchmetrics
Obsoletes:     %{name}-cloudwatchmetrics
Provides:      %{name}-codecommit%{?_isa} %{name}-codecommit
Obsoletes:     %{name}-codecommit
Provides:      %{name}-codedeploy%{?_isa} %{name}-codedeploy
Obsoletes:     %{name}-codedeploy
Provides:      %{name}-codepipeline%{?_isa} %{name}-codepipeline
Obsoletes:     %{name}-codepipeline
Provides:      %{name}-cognitoidentity%{?_isa} %{name}-cognitoidentity
Obsoletes:     %{name}-cognitoidentity
Provides:      %{name}-cognitoidp%{?_isa} %{name}-cognitoidp
Obsoletes:     %{name}-cognitoidp
Provides:      %{name}-cognitosync%{?_isa} %{name}-cognitosync
Obsoletes:     %{name}-cognitosync
Provides:      %{name}-config%{?_isa} %{name}-config
Obsoletes:     %{name}-config
Provides:      %{name}-core%{?_isa} %{name}-core
Obsoletes:     %{name}-core
Provides:      %{name}-datapipeline%{?_isa} %{name}-datapipeline
Obsoletes:     %{name}-datapipeline
Provides:      %{name}-devicefarm%{?_isa} %{name}-devicefarm
Obsoletes:     %{name}-devicefarm
Provides:      %{name}-directconnect%{?_isa} %{name}-directconnect
Obsoletes:     %{name}-directconnect
Provides:      %{name}-directory%{?_isa} %{name}-directory
Obsoletes:     %{name}-directory
Provides:      %{name}-discovery%{?_isa} %{name}-discovery
Obsoletes:     %{name}-discovery
Provides:      %{name}-dms%{?_isa} %{name}-dms
Obsoletes:     %{name}-dms
Provides:      %{name}-dynamodb%{?_isa} %{name}-dynamodb
Obsoletes:     %{name}-dynamodb
Provides:      %{name}-ec2%{?_isa} %{name}-ec2
Obsoletes:     %{name}-ec2
Provides:      %{name}-ecr%{?_isa} %{name}-ecr
Obsoletes:     %{name}-ecr
Provides:      %{name}-ecs%{?_isa} %{name}-ecs
Obsoletes:     %{name}-ecs
Provides:      %{name}-efs%{?_isa} %{name}-efs
Obsoletes:     %{name}-efs
Provides:      %{name}-elasticache%{?_isa} %{name}-elasticache
Obsoletes:     %{name}-elasticache
Provides:      %{name}-elasticbeanstalk%{?_isa} %{name}-elasticbeanstalk
Obsoletes:     %{name}-elasticbeanstalk
Provides:      %{name}-elasticloadbalancing%{?_isa} %{name}-elasticloadbalancing
Obsoletes:     %{name}-elasticloadbalancing
Provides:      %{name}-elasticsearch%{?_isa} %{name}-elasticsearch
Obsoletes:     %{name}-elasticsearch
Provides:      %{name}-elastictranscoder%{?_isa} %{name}-elastictranscoder
Obsoletes:     %{name}-elastictranscoder
Provides:      %{name}-emr%{?_isa} %{name}-emr
Obsoletes:     %{name}-emr
Provides:      %{name}-events%{?_isa} %{name}-events
Obsoletes:     %{name}-events
Provides:      %{name}-gamelift%{?_isa} %{name}-gamelift
Obsoletes:     %{name}-gamelift
Provides:      %{name}-glacier%{?_isa} %{name}-glacier
Obsoletes:     %{name}-glacier
Provides:      %{name}-iam%{?_isa} %{name}-iam
Obsoletes:     %{name}-iam
Provides:      %{name}-importexport%{?_isa} %{name}-importexport
Obsoletes:     %{name}-importexport
Provides:      %{name}-inspector%{?_isa} %{name}-inspector
Obsoletes:     %{name}-inspector
Provides:      %{name}-iot%{?_isa} %{name}-iot
Obsoletes:     %{name}-iot
Provides:      %{name}-kinesis%{?_isa} %{name}-kinesis
Obsoletes:     %{name}-kinesis
Provides:      %{name}-kms%{?_isa} %{name}-kms
Obsoletes:     %{name}-kms
Provides:      %{name}-lambda%{?_isa} %{name}-lambda
Obsoletes:     %{name}-lambda
Provides:      %{name}-logs%{?_isa} %{name}-logs
Obsoletes:     %{name}-logs
Provides:      %{name}-machinelearning%{?_isa} %{name}-machinelearning
Obsoletes:     %{name}-machinelearning
Provides:      %{name}-marketplacecommerceanalytics%{?_isa} %{name}-marketplacecommerceanalytics
Obsoletes:     %{name}-marketplacecommerceanalytics
Provides:      %{name}-marketplacemeteringservice%{?_isa} %{name}-marketplacemeteringservice
Obsoletes:     %{name}-marketplacemeteringservice
Provides:      %{name}-opsworks%{?_isa} %{name}-opsworks
Obsoletes:     %{name}-opsworks
Provides:      %{name}-pom%{?_isa} %{name}-pom
Obsoletes:     %{name}-pom
Provides:      %{name}-opsworks%{?_isa} %{name}-opsworks
Obsoletes:     %{name}-opsworks
Provides:      %{name}-rds%{?_isa} %{name}-rds
Obsoletes:     %{name}-rds
Provides:      %{name}-redshift%{?_isa} %{name}-redshift
Obsoletes:     %{name}-redshift
Provides:      %{name}-route53%{?_isa} %{name}-route53
Obsoletes:     %{name}-route53
Provides:      %{name}-s3%{?_isa} %{name}-s3
Obsoletes:     %{name}-s3
Provides:      %{name}-ses%{?_isa} %{name}-ses
Obsoletes:     %{name}-ses
Provides:      %{name}-simpledb%{?_isa} %{name}-simpledb
Obsoletes:     %{name}-simpledb
Provides:      %{name}-simpleworkflow%{?_isa} %{name}-simpleworkflow
Obsoletes:     %{name}-simpleworkflow
Provides:      %{name}-sns%{?_isa} %{name}-sns
Obsoletes:     %{name}-sns
Provides:      %{name}-sqs%{?_isa} %{name}-sqs
Obsoletes:     %{name}-sqs
Provides:      %{name}-ssm%{?_isa} %{name}-ssm
Obsoletes:     %{name}-ssm
Provides:      %{name}-storagegateway%{?_isa} %{name}-storagegateway
Obsoletes:     %{name}-storagegateway
Provides:      %{name}-sts%{?_isa} %{name}-sts
Obsoletes:     %{name}-sts
Provides:      %{name}-support%{?_isa} %{name}-support
Obsoletes:     %{name}-support
Provides:      %{name}-test-utils%{?_isa} %{name}-test-utils
Obsoletes:     %{name}-test-utils
Provides:      %{name}-waf%{?_isa} %{name}-waf
Obsoletes:     %{name}-waf
Provides:      %{name}-workspaces%{?_isa} %{name}-workspaces
Obsoletes:     %{name}-workspaces
Provides:      %{name}-javadoc%{?_isa} %{name}-javadoc
Obsoletes:     %{name}-javadoc

%description
The AWS SDK for Java enables Java developers to easily work with Amazon Web Services and build
scalable solutions with Amazon S3, Amazon DynamoDB, Amazon Glacier, and more.

%prep
%autosetup -n %{name}-9883b981ab5103cc6944fbf8f3b973994777350f -p1

sed -i '/NotThreadSafe/d' \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/CloudWatchMetricConfig.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/ApacheHttpClientConfig.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/AmazonWebServiceRequest.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/DefaultRequest.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/ClientConfiguration.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/RequestClientOptions.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/internal/ResettableInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/internal/ReleasableInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/ProgressInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/metrics/ServiceLatencyProvider.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/ExecutionContext.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/LengthCheckInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/AWSRequestMetrics.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/AWSRequestMetricsFullSupport.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfo.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfoFullSupport.java \
 aws-java-sdk-core/src/test/java/com/amazonaws/http/response/HttpResponseProxy.java

sed -i '/ThreadSafe/d' \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/FileLocks.java \
 aws-java-sdk-ssm/src/main/java/com/amazonaws/services/simplesystemsmanagement/AWSSimpleSystemsManagementClient.java \
 aws-java-sdk-ssm/src/main/java/com/amazonaws/services/simplesystemsmanagement/AWSSimpleSystemsManagementAsyncClient.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/AmazonHttpClient.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/conn/ssl/SdkTLSSocketFactory.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/impl/client/HttpRequestNoRetryHandler.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/impl/client/SdkHttpRequestRetryHandler.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/request/Progress.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/request/ProgressSupport.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/VersionInfoUtils.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/LengthCheckInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfoUnmodifiable.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBAsyncClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBStreamsClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBStreamsAsyncClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/Index.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/DynamoDB.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/Table.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/ScanApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/QueryApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/GetItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/PutItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/DeleteItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/ListTablesApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/UpdateItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/BatchGetItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/BatchWriteItemApi.java \
 aws-java-sdk-gamelift/src/main/java/com/amazonaws/services/gamelift/AmazonGameLiftClient.java \
 aws-java-sdk-gamelift/src/main/java/com/amazonaws/services/gamelift/AmazonGameLiftAsyncClient.java \
 aws-java-sdk-codecommit/src/main/java/com/amazonaws/services/codecommit/AWSCodeCommitClient.java \
 aws-java-sdk-codecommit/src/main/java/com/amazonaws/services/codecommit/AWSCodeCommitAsyncClient.java \
 aws-java-sdk-codedeploy/src/main/java/com/amazonaws/services/codedeploy/AmazonCodeDeployClient.java \
 aws-java-sdk-codedeploy/src/main/java/com/amazonaws/services/codedeploy/AmazonCodeDeployAsyncClient.java \
 aws-java-sdk-autoscaling/src/main/java/com/amazonaws/services/autoscaling/AmazonAutoScalingClient.java \
 aws-java-sdk-autoscaling/src/main/java/com/amazonaws/services/autoscaling/AmazonAutoScalingAsyncClient.java \
 aws-java-sdk-elasticsearch/src/main/java/com/amazonaws/services/elasticsearch/AWSElasticsearchClient.java \
 aws-java-sdk-elasticsearch/src/main/java/com/amazonaws/services/elasticsearch/AWSElasticsearchAsyncClient.java \
 aws-java-sdk-storagegateway/src/main/java/com/amazonaws/services/storagegateway/AWSStorageGatewayClient.java \
 aws-java-sdk-storagegateway/src/main/java/com/amazonaws/services/storagegateway/AWSStorageGatewayAsyncClient.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/MetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/PredefinedMetricTransformer.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/ServiceMetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/RequestMetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/provider/transform/DynamoDBRequestMetricTransformer.java \
 aws-java-sdk-elastictranscoder/src/main/java/com/amazonaws/services/elastictranscoder/AmazonElasticTranscoderClient.java \
 aws-java-sdk-elastictranscoder/src/main/java/com/amazonaws/services/elastictranscoder/AmazonElasticTranscoderAsyncClient.java \
 aws-java-sdk-elasticloadbalancing/src/main/java/com/amazonaws/services/elasticloadbalancing/AmazonElasticLoadBalancingClient.java \
 aws-java-sdk-elasticloadbalancing/src/main/java/com/amazonaws/services/elasticloadbalancing/AmazonElasticLoadBalancingAsyncClient.java

sed -i '/Immutable/d' \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/model/S3ObjectId.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/model/InstructionFileId.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/S3V4AuthErrorRetryStrategy.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/retry/RetryPolicy.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/retry/internal/AuthRetryParameters.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/ProgressEvent.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/auth/profile/internal/Profile.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/B.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/BS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/BOOL.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/L.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/M.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/N.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NULL.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NamedElement.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/Path.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/Precedence.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/PathOperand.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/RemoveAction.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/S.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/SS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/ArrayIndexElement.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/GetItemExpressionSpec.java \
 aws-java-sdk-cloudfront/src/main/java/com/amazonaws/auth/PEMObject.java

sed -i '/GuardedBy/d' \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/crypto/MultipartUploadCryptoContext.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBReflector.java

%pom_remove_plugin -r com.github.siom79.japicmp:japicmp-maven-plugin

%pom_disable_module aws-java-sdk-code-generator
%pom_disable_module aws-java-sdk-swf-libraries
%pom_disable_module aws-java-sdk-osgi
%pom_disable_module aws-java-sdk-codegen-maven-plugin

%pom_remove_dep :aws-java-sdk-swf-libraries aws-java-sdk

for file in src/samples/AmazonEC2SpotInstances-Advanced/CreateSecurityGroupApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/Requests.java \
 src/samples/AmazonEC2SpotInstances-Advanced/GettingStartedApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/InlineTaggingCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/InlineGettingStartedCodeSampleApp.java \
 src/samples/AmazonKinesisFirehose/batchPutInput.txt \
 src/samples/AmazonKinesisFirehose/putRecordInput.txt \
 src/samples/AmazonEC2SpotInstances-GettingStarted/Requests.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/CreateSecurityGroupApp.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/InlineGettingStartedCodeSampleApp.java \
 src/samples/AwsCloudFormation/CloudFormationSample.template \
 src/samples/AwsCloudFormation/CloudFormationSample.java; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm -rf $file.orig
done

%build
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-aws-java-sdk
%doc src/samples/* README.md
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}/*
%{_javadir}/%{name}/*.jar
/usr/share/maven*

%changelog
* Tue Dec 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11.3-7
- Package init
